from flask import Flask
from app import create_app
from Process_Engagement import Read_Engagement
from Process_Member import Read_Member
from Process_Phase import Read_Phase
from Process_Group_Member import Read_Group_Member


app = create_app()

if __name__ == "__main__":
    Read_Engagement()
    Read_Member()
    Read_Phase()
    Read_Group_Member()
    app.run(host="0.0.0.0", debug=True)
