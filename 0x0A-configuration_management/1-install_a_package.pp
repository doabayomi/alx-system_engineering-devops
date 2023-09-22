# Installing flask using pip3
package { 'flask-install':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3'
}
