#!/usr/bin/env python3

import struct
import binascii
import logging
from enum import Enum

from pyptfw.debug.loghelpers import pp, eprint, Lazy
logger = logging.getLogger()


class Ops(Enum):
    # action value observed in blkparse binary output
    # unclear on bit meanings, so unclear, but works currently at QD=1
    # TODO: find bit meanings and fill out with other ops
    # TODO: Might be other implications at higher QDs - experiment
    TRIM        = 0x2012
    WRITESYNC   = 0x001a
    READ        = 0x0011


class BlkParserBinFormat():
    """
    format operations into a blktrace queue entries, to be written binary file
    """
    magic = 0x65617407
    def __init__(self):
        self.fmt = struct.Struct(
                   # defintion from FIO code: blktrace_api.h
                   # struct blk_io_trace {
            "I "   #   __u32 magic;        /* MAGIC << 8 | version */
            "I "   #   __u32 sequence;     /* event number */
            "Q "   #   __u64 time;         /* in nanoseconds */
            "Q "   #   __u64 sector;       /* disk offset */
            "I "   #   __u32 bytes;        /* transfer length */
            "H H " #   __u32 action;       /* what happened */  Split into action (0x0001 is Q) and command
            "I "   #   __u32 pid;          /* who did it */
            "I "   #   __u32 device;       /* device identifier (dev_t) */
            "I "   #   __u32 cpu;          /* on what cpu did it happen */
            "H "   #   __u16 error;        /* completion error */
            "H "   #   __u16 pdu_len;      /* length of data after this trace */
            )
        self.curSequence = 0

    def newEntry(self, time, sector, xferlen, operation):
        self.curSequence += 1
        parms = (self.magic, self.curSequence, time, sector, xferlen, 0x0001, operation, 0, 0x10310001, 0, 0, 0)
        logger.debug(Lazy(lambda: pp.pformat(*parms)))
        return self.fmt.pack(*parms)

