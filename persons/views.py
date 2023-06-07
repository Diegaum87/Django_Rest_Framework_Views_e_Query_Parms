from rest_framework.views import APIView, Request, Response, status
from persons.models import Person
from django.forms.models import model_to_dict


class PersonView(APIView):
    def get(self, req: Request) -> Response:
        persons = Person.objects.all()

        person_list = []
        for person in persons:
            person_dict = model_to_dict(person)
            person_list.append(person_dict)

        return Response(person_list, status.HTTP_200_OK)

    def post(self, req: Request) -> Response:
        print(req.data)

        # ocreate já salva no banco
        person = Person.objects.create(**req.data)
        person_dict = model_to_dict(person)

        return Response(person_dict, status.HTTP_201_CREATED)


class PersonDetailView(APIView):
    def get(self, req: Request, person_id: int) -> Response:
        # person = Person.objects.get(id=person_id)
        # person_dict = model_to_dict(person)
        # return Response(person_dict, status.HTTP_200_OK)
        try:
            person = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return Response({"msg": "Person not found"}, status.HTTP_404_NOT_FOUND)
        person_dict = model_to_dict(person)
        return Response(person_dict, status.HTTP_200_OK)

    def delete(self, req: Request, person_id: int) -> Response:
        try:
            person = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return Response({"msg": "Person not found"}, status.HTTP_404_NOT_FOUND)

        person.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, req: Request, person_id: int) -> Response:
        try:
            person = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        for key, value in req.data.items():
            setattr(person, key, value)

        person.save()

        person_dict = model_to_dict(person)
        return Response(person_dict, status=status.HTTP_200_OK)
