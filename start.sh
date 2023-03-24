echo "Cloning Repo...."
git clone https://github.com/pdiskshortnearn/Pdiskshortnearnv2.git /Shortner-Converter-Bot-V2
cd /Pdiskshortnearnv2
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py
