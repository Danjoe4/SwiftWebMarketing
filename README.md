# based on
https://github.com/uideck/simple-bootstrap-5-template
# guide for prod
https://dev.to/thetrebelcc/how-to-run-a-flask-app-over-https-using-waitress-and-nginx-2020-235c


# handy, gets pid associated with port 
lsof -i :5000 
# then 
kill pid
# reset clock to sync signature (wsl2 bug)
sudo hwclock -s

# To connect #####
ssh -i .ssh/swiftwebmarketing_home_site.pem ubuntu@ec2-100-27-11-64.compute-1.amazonaws.com 
# add changes 
git fetch --all 
git reset --hard origin/main
# make a new detached session
sudo tmux new -s session
# or attach to existing session
sudo tmux attach -t session
# in tmux session
source env/bin/activate
# start the app
python3 app.py --prod
# Press Ctrl B and press D to close the session

# nginx 
sudo systemctl status nginx
make sure it is working

# dependencies
pip list 
add changes to requirements.txt manually
dev env can be messy and have extra packages but the prod env should be minimalist
