# holberton user login
exec { 'soft limit change':
  command  => 'sudo sed -i "/holberton soft/s/4/10000/" /etc/security/limits.conf',
  path     => '/usr/local/bin/:/bin/',
  provider => shell,
}

exec { 'hard limit change':
  command  => 'sudo sed -i "/holberton hard/s/5/100000/" /etc/security/limits.conf',
  path     => '/usr/local/bin/:/bin/',
  provider => shell,
}
