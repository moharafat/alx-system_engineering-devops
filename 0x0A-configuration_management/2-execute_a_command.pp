# Execute a command to kill a process named killmenow

exec { 'pkill':
  command => 'pkill -f killmenow',
  path    => '/bin:/usr/bin'
}