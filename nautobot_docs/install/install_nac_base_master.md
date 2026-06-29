 scp  -r "E:\AmitGupta\Project\NAC_BASE-master.7z"  ubuntu@172.17.152.138:/home/ubuntu/nautobotProject/
 sudo apt install p7zip-full
 7z x NAC_BASE-master.7z
 sudo scp -r NAC_BASE-master /home/nautobot/
/opt/nautobot_nac
 sudo scp -r NAC_BASE-master /home/nautobot/

sudo chown nautobot:nautobot /opt/nautobot_nac
sudo -iu nautobot
 sudo chown -R nautobot:nautobot /home/nautobot/NAC_BASE-master/


python3.13 -m venv /opt/nautobot_nac
 source /opt/nautobot_nac/bin/activate

 pip install --upgrade pip wheel setuptools

Update name [tool.poetry]
name = "nac_ssot_velo" to "naac_location_vrf_grid"




