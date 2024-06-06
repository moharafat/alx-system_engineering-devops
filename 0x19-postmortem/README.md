# Postmortem Project

With regard to ALX's DevOps project 0x17. Web stack debugging #3, at 14:00 (GMT+2), an error occured on the ubuntu container that was running Apache webserver that was provided by ALX, 
bash
  `curl -sI 127.0.0.1` which led to `HTTP/1.0 500 Internal Server Error`

## Debugging

1. The 1st thing I did was to check running process using `ps aux` there were 3 Apache process running, 2 `www-data `, and 1 `root`.

2. In terminal #1 I ran `strace` on the PID of the `root` Apache process, in teminal #2 I curled the server nothing occured.

3. I did the same thing but change the `root` PID with the `www-data` PID  and BINGO, I got a long error, but something stood out `-1 ENOENT (No such file or directory)`error,  beliver there was an attempt to atempt to accss t `/var/www/html/wp-includes/class-wp-locale.phpp`.

4. in the folder `/var/www/html/` using VI i entered each file and searched by using `/.phpp` and  BINGO  LOCATED `wp-settings.php` line 137

5. then its time to write a script that removes the extra "p"

6. Tested by using `curl -sI 127.0.0.1` and everything is fine 200 OK

## Summary

there was ann extra "p" in `wp-settings.php` that prevented the file `class-wp-locale.phpp` to load.
we just remooved it.




## Prevention

+ periodic testing
+ keep an eye[Monitor] to allert u when there is something happemns

