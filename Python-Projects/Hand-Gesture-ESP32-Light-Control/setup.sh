
echo 'Installing Python dependencies...'
pip install -r requirements.txt

echo 'Setting up serial port permissions...'
echo 'Checking current user groups:'
groups $USER

echo ''
echo 'To fix permission issues, run:'
echo 'sudo usermod -a -G dialout $USER'
echo 'sudo usermod -a -G tty $USER'
echo ''
echo 'Then logout and login again for changes to take effect.'

