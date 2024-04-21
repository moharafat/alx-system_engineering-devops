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

file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/home/ubuntu/.ssh/config',
  line   => '    PasswordAuthentication no',
}

file_line { 'Declare identity file':
  ensure => present,
  path   => '/home/ubuntu/.ssh/config',
  line   => '    IdentityFile ~/.ssh/school',
}
