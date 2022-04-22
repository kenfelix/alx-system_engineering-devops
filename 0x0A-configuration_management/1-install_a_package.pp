# Installs flask
package { 'Flask 2.1.0':
  ensure   => '2.1.0',
  name     => 'Flask 2.1.0',
  provider => 'pip3'
}
