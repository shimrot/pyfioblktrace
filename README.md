pyfioblktrace
=============

What is it?
-----------

A python3 module which generates blktrace type binary entries, which can be used to  
generate blktrace replay files for use with fio.

The current attempt is minimal, and could use some help filling out other operations 
and variations. During 'replay' destination device needs to be overridden via the fio
replay_redirect option (the generated value is a dummy).

Currently it just generates 'Q' type entries.  Not sure if that is the only requirement, 
as a replay appears to occur a little faster than timing within the file.

Currently, writing the binary file and timings are an exercise for the user.   

 