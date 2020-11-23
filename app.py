import os
import shutil
import csv
import sys
from flask import Flask,render_template, url_for, flash, redirect, request
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_bootstrap import Bootstrap
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired
# import MySQLdb
import pymysql.cursors
import pymysql

app = Flask(__name__)
bootstrap = Bootstrap(app)

# Configurations
app.config['SECRET_KEY'] = 'blah blah blah blah'


connection = pymysql.connect(host="localhost",    
                     user="admin",        
                     passwd="root",  
                     db="security", port=3308)

connectionCursor = connection.cursor()


# ROUTES!
@app.route('/', methods=['GET', 'POST'])
def index():


    # Execution of query
    query = "select * from USER_ACCOUNT"
    connectionCursor.execute(query)
    # fetch the reults
    userAccountResult = connectionCursor.fetchall()

    
    # Execution of query
    query = "select * from USER_ROLE"
    connectionCursor.execute(query)
    # fetch the reults
    userRoleResult = connectionCursor.fetchall()

    # Execution of query
    query = "select * from PRIVILEGES"
    connectionCursor.execute(query)
    # fetch the reults
    privilegeResult = connectionCursor.fetchall()

    # Execution of query
    query = "select * from ACCOUNT_PRIVILEGES"
    connectionCursor.execute(query)
    # fetch the reults
    accountPrivilegeResult = connectionCursor.fetchall()

    # Execution of query
    query = "select * from RELATION_PRIVILEGES"
    connectionCursor.execute(query)
    # fetch the reults
    relationPrivilegeResult = connectionCursor.fetchall()

    # Execution of query
    query = "select * from Tables"
    connectionCursor.execute(query)
    # fetch the reults
    tablesResult = connectionCursor.fetchall()

    # Execution of query
    query = "select * from HAS_ON"
    connectionCursor.execute(query)
    # fetch the reults
    has_on_Result = connectionCursor.fetchall()


    return render_template('index.html',userAccountResult=userAccountResult, userRoleResult=userRoleResult, 
        privilegeResult=privilegeResult,accountPrivilegeResult=accountPrivilegeResult,
        relationPrivilegeResult=relationPrivilegeResult, tablesResult=tablesResult, has_on_Result=has_on_Result)


@app.route('/showCreateUserForm')
def showCreateUserForm():
    
    # Execution of query
    query = "select * from USER_ROLE"
    connectionCursor.execute(query)
    # fetch the reults
    roleIdNoResult = connectionCursor.fetchall()

    return render_template('showCreateUserForm.html', roleIdNoResult=roleIdNoResult)

    

    
@app.route('/createUserForm', methods=['GET', 'POST'])
def createUserForm():
    
    # fetch entered value from the form
    idNo = request.form['idNo']
    userName = request.form['userName']
    birthDate = request.form['birthDate']
    address = request.form['address']
    sex = request.form['sex']
    phoneNo = request.form['phoneNo']
    roleIdNo = request.form['roleIdNo']

    # Execution of query
    query = "INSERT INTO USER_ACCOUNT values ('"+idNo+"', '"+userName+"','"+birthDate+"','"+address+"', '"+sex+"', '"+phoneNo+"', '"+roleIdNo+"');"
    connectionCursor.execute(query)

    # fetch the reults
    roleIdNoResult = connectionCursor.fetchall()
    connection.commit()

    return redirect('/')

@app.route('/showCreateUserRoleForm')
def showCreateUserRoleForm():
    
    return render_template('showCreateUserRoleForm.html')


@app.route('/createUserRoleForm', methods=['GET', 'POST'])
def createUserRoleForm():
    
    # fetch entered value from the form
    roleIdNo = request.form['roleIdNo']
    roleName = request.form['roleName']
    description = request.form['description']

    # Execution of query
    query = "INSERT INTO USER_ROLE values ('"+roleIdNo+"', '"+roleName+"','"+description+"');"
    connectionCursor.execute(query)

    # fetch the reults
    roleIdNoResult = connectionCursor.fetchall()
    connection.commit()

    return redirect('/')





@app.route('/showCreatePrivilegesForm')
def showCreatePrivilegesForm():
    

    return render_template('showCreatePrivilegesForm.html')


@app.route('/createPrivilegesForm', methods=['GET', 'POST'])
def createPrivilegesForm():
    
    # fetch entered value from the form
    privilegeType = request.form['privilegeType']
    IdNo = request.form['IdNo']
    functionalityName = request.form['functionalityName']
    functionalityDescription = request.form['functionalityDescription']
    roleIdNumber = request.form['roleIdNumber']
    privilegeIdNumber = request.form['privilegeIdNumber']

    if(privilegeType == "Account_Privilege_Type"):
        query = "INSERT INTO ACCOUNT_PRIVILEGES values ('"+IdNo+"', '"+functionalityName+"','"+functionalityDescription+"','"+roleIdNumber+"','"+privilegeIdNumber+"')";
    else:
        query = "INSERT INTO RELATION_PRIVILEGES values ('"+IdNo+"', '"+functionalityName+"','"+functionalityDescription+"','"+roleIdNumber+"','"+privilegeIdNumber+"')";


    connectionCursor.execute(query)

    roleIdNoResult = connectionCursor.fetchall()
    connection.commit()

    return redirect('/')





@app.route('/showCreateTablesForm')
def showCreateTablesForm():
    
    # Execution of query
    query = "select * from USER_ACCOUNT"
    connectionCursor.execute(query)
    # fetch the reults
    IdNoResult = connectionCursor.fetchall()

    return render_template('showCreateTablesForm.html', IdNoResult=IdNoResult)


@app.route('/createTablesForm', methods=['GET', 'POST'])
def createTablesForm():
    
    # fetch entered value from the form
    tableId = request.form['tableId']
    tableName = request.form['tableName']
    description = request.form['description']
    idNo = request.form['idNo']

    # Execution of query
    query = "INSERT INTO Tables values ('"+tableId+"', '"+tableName+"','"+description+"','"+idNo+"');"
    connectionCursor.execute(query)

    # fetch the reults
    roleIdNoResult = connectionCursor.fetchall()
    connection.commit()

    return redirect('/')






@app.route('/showTransaction5')
def showTransaction5():
    
    return render_template('showTransaction5.html')

@app.route('/transaction5form', methods=['GET', 'POST'])
def transaction5form():
    
    # fetch entered value from the form
    roleIdNo = request.form['roleIdNo']
    IdNo = request.form['IdNo']

    # Execution of query
    query = "UPDATE USER_ACCOUNT set Role_Id='"+roleIdNo+"' where IdNo='"+IdNo+"'"
    connectionCursor.execute(query)

    # fetch the reults
    roleIdNoResult = connectionCursor.fetchall()
    connection.commit()

    return redirect('/')


@app.route('/showTransaction6')
def showTransaction6():
    

    return render_template('showTransaction6.html')

@app.route('/transaction6form', methods=['GET', 'POST'])
def transaction6form():
    
    # fetch entered value from the form
    roleIdNo = request.form['roleIdNo']
    accountIdNo = request.form['accountIdNo']

    # Execution of query
    query = "UPDATE ACCOUNT_PRIVILEGES set Role_Id='"+roleIdNo+"' where Account_Id='"+accountIdNo+"'"
    connectionCursor.execute(query)

    # fetch the reults
    roleIdNoResult = connectionCursor.fetchall()
    connection.commit()

    return redirect('/')


@app.route('/showTransaction7')
def showTransaction7():
    

    return render_template('showTransaction7.html')
    
@app.route('/transaction7form', methods=['GET', 'POST'])
def transaction7form():
    
    # fetch entered value from the form
    roleIdNo = request.form['roleIdNo']
    tableIdNo = request.form['tableIdNo']

    # Execution of query
    query = "UPDATE HAS_ON set Role_Id='"+roleIdNo+"' where Table_Id='"+tableIdNo+"' and Privilege_Id='P02'"
    connectionCursor.execute(query)

    # fetch the reults
    result1 = connectionCursor.fetchall()
    print(result1)
    connection.commit()

    return render_template('showTransaction7.html', result1=result1)




@app.route('/showTransaction8a')
def showTransaction8a():
    

    return render_template('showTransaction8a.html')
    
@app.route('/transaction8formRole', methods=['GET', 'POST'])
def transaction8formRole():
    
    # fetch entered value from the form
    roleIdNo = request.form['roleIdNo']

    # Execution of query
    query1 = "SELECT Account_Functionality_name from ACCOUNT_PRIVILEGES , USER_ROLE where ACCOUNT_PRIVILEGES.Role_id=USER_ROLE.Role_id and USER_ROLE.Role_id='"+roleIdNo+"'"
    connectionCursor.execute(query1)

    result1 = connectionCursor.fetchall()

    query2="SELECT Relation_Functionality_name from USER_ROLE, HAS_ON , RELATION_PRIVILEGES where USER_ROLE.Role_id='"+roleIdNo+"' and USER_ROLE.Role_id = HAS_ON.Role_id and HAS_ON.Relation_Id=RELATION_PRIVILEGES.Relation_Id"
    connectionCursor.execute(query2)
    
    # fetch the reults
    result2 = connectionCursor.fetchall()
    connection.commit()

    return render_template('showTransaction8a.html', result1=result1, result2=result2)
    


@app.route('/showTransaction8b')
def showTransaction8b():
    

    return render_template('showTransaction8b.html')

@app.route('/transaction8formAccount', methods=['GET', 'POST'])
def transaction8formAccount():
    
    # fetch entered value from the form
    accountIdNo = request.form['accountIdNo']
    print(accountIdNo)
    # Execution of query
    query1 = "SELECT Account_Functionality_name from account_privileges, user_account, user_role where IdNo='"+accountIdNo+"' and ACCOUNT_PRIVILEGES.Role_id=USER_ROLE.Role_id and USER_ACCOUNT.Role_Id=USER_ROLE.Role_id"
    connectionCursor.execute(query1)

    result1 = connectionCursor.fetchall()

    query2="SELECT Relation_Functionality_name from USER_ACCOUNT, USER_ROLE, HAS_ON , RELATION_PRIVILEGES where IdNo='"+accountIdNo+"' and USER_ACCOUNT.Role_Id=USER_ROLE.Role_id and USER_ROLE.Role_id = HAS_ON.Role_id and HAS_ON.Relation_Id=RELATION_PRIVILEGES.Relation_Id"
    connectionCursor.execute(query2)
    
    # fetch the reults
    result2 = connectionCursor.fetchall()
    connection.commit()
    print(result1)
    return render_template('showTransaction8b.html', result1=result1, result2=result2)





@app.errorhandler(404)
@app.route("/error404")
def page_not_found(error):
    return render_template('404.html',title='404')

@app.errorhandler(500)
@app.route("/error500")
def requests_error(error):
    print(error)
    return render_template('500.html',title=error)

port = int(os.getenv('PORT', '3000'))
app.run(host='0.0.0.0', port=port)
