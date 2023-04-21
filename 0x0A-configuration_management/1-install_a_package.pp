# Installs flask, version 2.1.1

package { 'python3-flask':
  ensure   => '2.1.0',
  provider => 'gem',
}
