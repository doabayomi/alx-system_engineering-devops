# stack fix to zero errors
exec { 'stack fix':
  command  => 'sudo sed -i "s/15/4096/g" /etc/default/nginx; sudo service nginx restart',
  provider => shell,
}
