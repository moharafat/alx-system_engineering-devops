file { '/home/ubuntu/.ssh':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0700',
}

file { '/home/ubuntu/.ssh/config':
  ensure  => present,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
  content => "
    Host 54.173.50.211
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
