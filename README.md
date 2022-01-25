# Python och programmering

## TIPS: conda environments med jupyter notebook

#### 1. Skapa ett nytt conda environment

Skapa ditt environment och installera `python` och `ipykernel`. __Välj själv namn istället för NEW_ENV__. `ipykernel` är för att skapa en Jupyter Notebook.

	conda create --name NEW_ENV python=3.9 ipykernel

#### 2. Aktivera din NYA environment

	conda activate NEW_ENV

Man ser att miljön är aktiverad geonom att det står (NEW_ENV) i terminalen. __FÖRSTA GÅNGEN__ du aktiverar din miljö ska du inte glömma att installera alla requirements. Se till att du har din environment aktiverad och står i samma mapp (folder) som din `requirements.txt` fil finns genom att titta på listan som dyker upp när du kör

	ls
Man kan byta mapp med 

	cd DIRECTORY_NAME

När du ser att din `requirements.txt`-fil finns så kör du

	pip install -r requirements.txt


#### 4. Skapa en notebook i VSCode

1. I VSCode, skapa en ny notebook med ctrl + shift + p
2. Sök på 'Jupyter: Create New Blank Notebook' och välj det
3. I övre högra hörnet finns en knapp för att välja kernel. Tryck på den och sök på din NEW_ENV

## TIPS: Ta bort environments
För att se vilka enviroments som finns skapat skriva 

	conda env list

För att radera ett environment börja med att deaktivera det enviromentet så att man är i (base)

	conda deactivate

För att radera ett environment skriva

	conda env remove --name ENV_NAME

ENV_NAME är namnet på environmentet som ska raderas.

## TIPS: git + kursens repo = sant

Det är ett repository för kursen. För att få ner det lokalt på din dator behöver du öppna en terminal och använda git-kommandon enligt följande instruktioner:

#### 1. Öppna din terminal och navigera till en plats på din dator där du vill ha kursmaterialet

#### 2. Skriv in följande kommando i terminalen:
	
	git clone https://github.com/evahegnar/python_programmering

#### 3. Öppna mappen genom kommandot 
	
	cd python_programmering

#### 4. Skapa nu en ny virtual environment med hjälp av conda och aktivera den.

I mappen du står i finns det en fil som heter requirements.txt. Den filen innehåller en lista på pythonpaket som du ska installera i din conda environment. 

Mappen kommer uppdateras och för att få de senaste ändringarna använder ni git pull

	git pull

Om ni väljer att jobba i detta repositroy, vilket kan vara skönt med all kursmaterial lättillgänglig, kan ni inte pusha egna ändringar till repot. Ni kan dock committa till er lokala Git repo och ha det sparat lokalt. 

	git add FILE_NAME
	git commit -m "comment about changes"

Om du vill kunna ladda ner de senaste ändringarna i kursens GitHub repo, men bara får en massa erorrs, följ dessa steg:

#### 1. git status
För att se vilka filer som din git klagar på, gör detta kommando
	
	git status

Titta speciellt på filerna som dyker upp under rubriken __changes not staged for commit__. De kommer att dyka upp med röd text.

Om det är ändringar som du inte vill spara, gå till steg 2. Om du har ändringar du vill spara, gå vidare till steg 3.

#### 2. git revert

I den röda texten specificeras vägen till de filer som du ska återställa (alltså det som du inte vill spara). Du återställer genom att köra

	git revert path-to-file

för varje path-to-file som synts i rött. Om du provar att göra `git status` igen så ska inga filer finnas kvar under __changes not staged for commit.__

Då kan du gå vidare till att dra ner det senaste i repot genom

	git pull

#### 3. git add och git commit

I den röda texten specificeras vägen till de filer som du vill spara ändringarna i. Du sparar genom att köra
	
	git add path-to-file

för varje path-to-file som synts i rött. Om du provar att göra `git status` igen så ska dessa filer dyka upp som gröna istället.

När du inte har några filer kvar under __changes not staged for commit__ så kan du gå vidare till att dra ner det senaste i repot genom

	git pull


## Forking

Om ni vill pusha upp era commits någonstans så att de är sparade på GitHub molnet så kan ni forka repot och klona eran fork istället.

 - [Generellt om fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks)
 - [Hur man gör en fork](https://docs.github.com/en/enterprise-server@3.0/get-started/quickstart/fork-a-repo)
 - [Hur man håller koll på origanl repo och fork samtidigt med remote](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/configuring-a-remote-for-a-fork)
 - [Hur man hämtar ner det senaste lärare gjort på föreläsningsrepo (fetch)](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork)
 - [Föra in det senaste läraren har gjort till ditt egna arbete (merge)](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/merging-an-upstream-repository-into-your-fork )
 - [Hur ändra till fork om man redan har kopierat (copy) ett repo](https://admcpr.com/what-the-fork/)



## Kurslitteratur

Vi kommer använda många olika resurser för att lära oss om python, men vi kommer till stor del att använda oss av Jake VanderPlas *A whirlwind tour of python* och *Python data science handbook*. 
Båda böckerna är gratis och tillgängliga på författarens github både som text och som jupyter notebooks. För att ta till sig materialet rekommenderar vi starkt att ni kör all kod själva när ni läser!

Länkar till böckerna:
- [WIP](https://jakevdp.github.io/WhirlwindTourOfPython/) 
- [PDS handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)



## Data Camp

Vi har ett premium medlemskap till Data Camp Classroom. Data Camp är en platform med kurser och övningar inom Data Science. Denna kan ni använda för att komplettera utbildningen. 

För att få fri tillång måste ni följa denna länken [Data Camp Classroom](https://www.datacamp.com/groups/shared_links/1e9ec73fbf3dd46f0a0a9c8a9e773774c7ad2add6677109d698782ea059a2ae3) och skapa ett konto med studentmailen *@utb.ecutbildning.se*  
 
