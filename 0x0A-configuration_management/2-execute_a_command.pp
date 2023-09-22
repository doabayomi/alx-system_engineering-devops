# Killing a process using pkill
exec { 'killmenow':
  command => '/usr/bin/pkill -f "./killmenow"'
}
