# Przykład usługi REST w języku Python oraz testy Postman zaimplementowanej usługi

W pliku books.json znajdują się dane, używane w zaimplementowanej usłudze sieciowej REST.

W pliku rest-service.py znajduje się program, w języku Python, korzystający z biblioteki Flask. Jest to usługa REST, pobierająca dane ze wskazanego pliku books.json i zwracająca je w formacie JSON. Usługa umożliwia również zmianę tytułu książki, wskazując odpowiedni numer ISBN książki i podając nowy tytuł książki.

Przykładowe wywołania usługi znajdują się w testach, utworzonych w programie Postman, znajdujących się w folderze postman_tests.
