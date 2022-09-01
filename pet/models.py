from django.db import models

ESPECIE_CHOICES = (
	('cachorro', 'Cachorro'),
	('gato', 'Gato'),
	('coelho', 'Coelho'),
	('cavalo', 'Cavalo'),
	('peixe', 'Peixe')
)

RACA_CACHORRO = (

	('1','Afegão Hound'),
	('2','Affenpinscher'),
	('3','Airedale Terrier'),
	('4', 'Akita'),
	('5','American Staffordshire Terrier'),
	('6','Basenji'),
	('7','Basset Hound'),
	('8','Beagle'),
	('9','Beagle Harrier'),
	('10','Bearded Collie'),
	('11','Bedlington Terrier'),
	('12','Bichon Frisé'),
	('13','Bloodhound'),
	('14','Bobtail'),
	('15','Boiadeiro Australiano'),
	('16','Boiadeiro Bernês'),
	('17','Border Collie'),
	('18','Border Terrier'),
	('19','Borzoi'),
	('20','Boston Terrier'),
	('21','Boxer'),
	('22','Buldogue Francês'),
	('23','Buldogue Inglês'),
	('24','Bull Terrier'),
	('25','Bulmastife'),
	('26','Cairn Terrier'),
	('27','Cane Corso'),
	('28','Cão de Água Português'),
	('29','Cão de Crista Chinês'),
	('30','Cavalier King Charles Spaniel'),
	('31','Chesapeake Bay Retriever'),
	('32','Chihuahua'),
	('33','Chow Chow'),
	('34','Cocker Spaniel Americano'),
	('35','Cocker Spaniel Inglês'),
	('36','Collie'),
	('37','Coton de Tuléar'),
	('38','Dachshund'),
	('39','Dálmata'),
	('40','Dandie Dinmont Terrier'),
	('41','Dobermann'),
	('42','Dogo Argentino'),
	('43','Dogue Alemão'),
	('44','Fila Brasileiro'),
	('45','Fox Terrier (Pelo Duro e Pelo Liso)'),
	('46','Foxhound Inglês'),
	('47','Galgo Escocês'),
	('48','Galgo Irlandês'),
	('49','Golden Retriever'),
	('50','Grande Boiadeiro Suiço'),
	('51','Greyhound'),
	('52','Grifo da Bélgica'),
	('53','Husky Siberiano'),
	('54','Jack Russell Terrier'),
	('55','King Charles'),
	('56','Komondor'),
	('57','Labradoodle'),
	('58','Labrador Retriever'),
	('59','Lakeland Terrier'),
	('60','Leonberger'),
	('61','Lhasa Apso'),
	('62','Lulu da Pomerânia'),
	('63','Malamute do Alasca'),
	('64','Maltês'),
	('65','Mastife'),
	('66','Mastim Napolitano'),
	('67','Mastim Tibetano'),
	('68','Norfolk Terrier'),
	('69','Norwich Terrier'),
	('70','Papillon'),
	('71','Pastor Alemão'),
	('72','Pastor Australiano'),
	('73','Pinscher Miniatura'),
	('74','Poodle'),
	('75','Pug'),
	('76','Rottweiler'),
	('77','Sem Raça Definida (SRD)'),
	('78','ShihTzu'),
	('79','Silky Terrier'),
	('80','Skye Terrier'),
	('81','Staffordshire Bull Terrier'),
	('82','Terra Nova'),
	('83','Terrier Escocês'),
	('84','Tosa'),
	('85','Welsh Corgi (Cardigan)'),
	('86','Welsh Corgi (Pembroke)'),
	('87','West Highland White Terrier'),
	('88','Whippet'),
	('90','Xoloitzcuintli'),
	('91','Yorkshire Terrier')
	
)

TEMPERAMENTO_CHOICES =(
	('1','Agressivo'),
    ('2','Manso'),
    ('3','Anti-social'),
    ('4','Social'),
    ('5','Agitado'),
    ('6','Calmo'),
    ('7','Introvertido'),
    ('8','Extrovertido'),
    ('9','Obediente'),
    ('10','Independente'),
    ('11','Curioso'),
    ('12','Indiferente'),
    ('13','Ousado'),
    ('14','Tímido'),
)
PELAGEM_CHOICES = (
	('1','Levemente Aspera'),
	('2', 'Fios Lisos e Longos')
)
COLORACAO_CHOICES = (
	('amarelo', 'Amarelo'),
	('branco', 'Branco'),
	('caramelo', 'Caramelo'),
	('marrom', 'Marrom'),
	('preto','Preto')
)

class formPet(models.Model):
	nome = models.CharField('Nome',max_length=150)
	apelido = models.CharField('Apelido',max_length=30)
	aniversario = models.DateField('Aniversário', blank=True, null=True)
	idade = models.IntegerField('Idade')
	peso = models.IntegerField('Peso(kg)')
	tamanho = models.IntegerField('Tamanho')
	especie = models.CharField('Especie',max_length=10, choices=ESPECIE_CHOICES)
	racaCachorro = models.CharField('Raça do Cachorro',max_length=3, choices=RACA_CACHORRO)
	temperamento = models.CharField('Temperamento',max_length=3, choices=TEMPERAMENTO_CHOICES)
	pelagem = models.CharField('Pelagem',max_length=2, choices=PELAGEM_CHOICES)
	coloracao = models.CharField('Coloração',max_length=10, choices=COLORACAO_CHOICES)
	tamanho = models.IntegerField('Tamanho(cm)',)
	caracteristicas = models.CharField('Caracteristicas', max_length=200)
	def __str__(self):
		return self.nome	

	


