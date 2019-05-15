To run this Project required installations:

 --> Install python3:
        sudo apt-get install python3.6

 --> Install pip3 using command:
      sudo apt-get install python3 python3-pip 

 --> Install django using command:
       pip3 install Django

 --> Install MySQL and mySQL client using commands:
     sudo apt-get install mysql-server 
     sudo apt-get install libmysqlclient-dev python3-dev
	 pip3 install --user mysqlclient-1.3.13.tar.gz 

 --> A SQL database is required to run this project.
      I was dumped my database in a file management2.sql using command :
             mysqldump -u root -p databasename > filename.sql (Mysql password)

      Create a database in SQL , create a file and Dump this database to your computer using command:
             mysql -u root -p databasename < filename.sql (Mysql password) 
 
After all installations run this project in terminal using command:
      --> cd Filename
      --> python3 manage.py runserver 8080  
