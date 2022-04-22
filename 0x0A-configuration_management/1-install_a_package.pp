# Installs flask
python::pip { 'pip3 install flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3'
}
