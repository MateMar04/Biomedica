# Create your tests here.
from django.test import TestCase

from .models import *


class MedicoTestCase(TestCase):
    def setUp(self):
        Medico.objects.create(nombre="Pepe", apellido="Garcia", matricula="ndgfkjnf")
        Medico.objects.create(nombre="Andres", apellido="Gonzalez", matricula="adssgfkq")

    def test_medico_is_valid(self):
        pepe = Medico.objects.get(name="Pepe")
        andres = Medico.objects.get(name="Andres")

        self.assertEqual(pepe.matricula, "ndgfkjnf")
        self.assertEqual(andres.apellido, "Gonzalez")
