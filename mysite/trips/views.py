#native
from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
import json

#custom
from .SQL_Connector import Database

def hello_world(request):
    return render(request,
                  'hello_world.html',
                  {'current_time': datetime.now()})

def read_post(request):
    classification=request.POST['classification']
    SQL=Database('root','Airbus@a380','128.199.241.131',13388,'NTUST_Talk')
    stmt="SELECT `author`,`content`,`date`,`sid` FROM `Posts` Where `classfication` = %(Classifications)s ORDER BY `date` DESC" 
    PostSearch=SQL.Query(stmt,{'Classifications':classification})
    Result=[]
    for post in PostSearch:
        Post={}
        Post["作者"]=post[0]
        Post["內容"]=post[1]
        Post["日期"]=str(post[2])
        Post["User_ID"]=post[3]
        Result.append(Post)
    return HttpResponse(json.dumps(Result,ensure_ascii=False))

def write_post(request):
    author=request.POST['author']
    classification=request.POST['classification']
    Post_Content=request.POST['Post_Content']
    User_ID=request.POST['User_ID']
    date=request.POST['date']
    SQL=Database('root','Airbus@a380','128.199.241.131',13388,'NTUST_Talk')
    stmt = ("INSERT INTO  `Posts`(`author`,`content`,`classfication`,`sid`,`date`) "
                "VALUES (%s,%s,%s,%s,%s)")
    data = (author,Post_Content,classification,User_ID,date)
    SQL.Update(stmt,data)
    return HttpResponse("Success")

def main():
    SQL=Database('root','Airbus@a380','128.199.241.131',13388,'User')
    stmt="SELECT `born` FROM `User_Data`"
    PostSearch=SQL.Query(stmt)
    print(PostSearch)

# main()