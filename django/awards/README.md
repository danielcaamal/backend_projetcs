# Django Awards

# To install

1. Execute the docker-compose file
> - $ sudo docker-compose up -d --build
2. Run the migrations
> - $ docker-compose exec web python manage.py migrate --noinput
3. Ensure Django table were created
> - $ docker-compose exec db psql --username=postgres --dbname=postgres

Notes:
- Change the permission (if apply)
> - $ sudo chown -R $USER:$USER .

- If there is not way, first try:
> - docker-compose down --volumes 

- If not:
> - docker system prune -a --volumes

