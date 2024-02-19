# Minitrice

## Installation
### WSL 

Pour installer WSL (Windows Subsystem for Linux) sur votre ordinateur :
- Assurez-vous d'avoir au moins Windows 10 ou ultérieure.
- Ouvrez PowerShell en tant qu'administrateur et exécutez cette commande pour activer le sous système linux:
````bash
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
````
- Redémarrez votre ordinateur.
- Installez une distribution Linux depuis Microsoft Store.
- Lancez la distribution Linux et configurez un nom d'utilisateur et un mot de passe.
- Une fois installé, vous pouvez exécuter des commandes Linux directement depuis l'invite de commandes Windows ou PowerShell.

### Prérequis pour le programme minitrice
Pour pouvoir exécuter le programme minitrice, il faut s'assurer que vous avez les permissions pour lancer le script. C'est à dire quand vous faite la commande ll ou ls -l il faut que dans les permissions du script minitrice, on a des x qui permet de nous dire que l'on peut exécuter ce script. 
## Exécution

### Utilisation interactive
#### Scénario 1:
- Lancer le programme minitrice en faisant la commande ./minitrice
- Entrer une expression mathématique (par exemple, "3+9") de cette façon > 3+9
- Le programme affiche le résultat du calcul (par exemple, "12").
- Entrer une nouvelle expression ou quitter en appuyant sur `ctrl+D`.
Le programme affiche "Fin des calculs :)".
Le code de sortie du programme est 0, indiquant une exécution réussie.

Exemple d'utilisation :

```bash
$ ./minitrice
> 3+9
12
> 4*5
20
> 13-6
7
>
Fin des calculs :)
$ echo $?
0
$ 
```

### Utilisation en lisant STDIN avec `echo`
#### Scénario 2:
- Utiliser la commande echo pour envoyer une expression mathématique (par exemple, "3+12") au programme minitrice via STDIN.
- Le programme minitrice calcule le résultat de l'expression (par exemple, "15") et l'affiche.
- Le code de sortie du programme est 0, indiquant une exécution réussie.

Exemple d'utilisation :

```bash
$ echo "3+12" | ./minitrice
15
$ echo $?
0
$ 
```

### Utilisation en lisant STDIN avec `cat`
#### Scénario 4:
- Utiliser la commande `cat` pour envoyer les expressions contenues dans un fichier (par exemple, good-expression.txt) au programme minitrice via STDIN.
- Le programme minitrice calcule le résultat de chaque expression et les affiche séparément.
- Une fois toutes les expressions traitées, le code de sortie du programme est 0, indiquant une exécution réussie.
  
Exemple d'utilisation avec un fichier contenant des expressions :

```bash
$ cat good-expression.txt | ./minitrice
4
11
35
-4
12
90
4.0
8.0
10
4
$ echo $?
0
$ 
```

## Gestion d'erreurs

### Erreur de syntaxe
#### Scénario 4:
- Utiliser la commande echo pour envoyer une expression mathématique contenant une erreur de syntaxe (par exemple, "3+*12") au programme minitrice via STDIN.
- Le programme minitrice détecte l'erreur de syntaxe et affiche un message d'erreur indiquant la nature de l'erreur ("Erreur de syntaxe pour le calcul: "3+*12").
- Le code de sortie du programme est 1, indiquant une erreur lors de l'exécution.

En cas d'erreur de syntaxe, le programme affiche un message d'erreur et renvoie un code de sortie 1.

Exemple :

```bash
$ echo "3+*12" | ./minitrice
Erreur de syntaxe pour le calcul: "3+*12"
$ echo $?
1
$ 
```

### Division par zéro
#### Scénario 5: 

- Utiliser la commande echo pour envoyer une expression mathématique contenant une division par zéro (par exemple, "3/0") au programme minitrice via STDIN.
- Le programme minitrice détecte la division par zéro et affiche un message d'erreur spécifique ("Division par zéro").
- Le code de sortie du programme est 1, indiquant une erreur lors de l'exécution.
- En cas de division par zéro, le programme affiche un message d'erreur spécifique et renvoie un code de sortie non nul.

Exemple :

```bash
$ echo "3/0" | ./minitrice
Division par zéro
$ echo $?
1
$ 
```

## Générateur d'expression

Le programme Minitrice peut être combiné avec le programme Generator pour générer des expressions aléatoires et les évaluer.

Exemple d'utilisation avec Generator :

```bash
$ ./generator 2 | ./minitrice
-2
7.0
$
```

## Bonus : Gestion d'erreur dans le générateur d'expression

Le générateur d'expression peut générer des erreurs, par exemple une erreur dans la génération des expressions ou une erreur dans les opérations. Ces erreurs ne sont pas gérées pour l'instant mais pourraient être implémentées comme un bonus dans le développement futur du programme.





## Generator
Le programme ``generator.py`` va servir à générer des expressions aléatoires. Il devra être coupler/piper avec le programme principal qui est ``minitrice.py``.

Son utilisation se fait de la manière suivante: ``python generator.py <n>``, ``n`` étant le nombre d'expressions que l'on veut générer.
