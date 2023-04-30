# datagen-podcast
<p align="center">
  <img src="data-gen.png">
</p>

Semantic search to query transcription from [Data Gen](https://open.spotify.com/show/27XP61URSuKu9oeWR793D6)
Inspired by [Ben Trevett](https://github.com/bentrevett/lexisearch) and [James Briggs](https://www.youtube.com/watch?v=vpU_6x3jowg).

I use [spotify-dlx](https://pypi.org/project/spotify-dlx/) to download audio and [Whisper JAX](https://github.com/sanchit-gandhi/whisper-jax) to make the transcription.


Example of query

`python query_index.py --query "Qu'est-ce qui t'a le plus fait progresser ?"`

Output:

```markdown
title: #20 - Gorgias : Migrer vers la Modern Data Stack
transcript: [2138.08 ====> 2161.6]  Donc voilà, la transversalité.  
Qu'est-ce qui t'a le plus fait progresser ?  C'est un peu cliché, 
mais c'est vraiment de mettre les mains dedans, de faire.  
Moi, j'ai toujours appris comme ça déjà pendant les études, etc.  
Faire une forme de freelance à côté.  Vraiment en faisant, c'est là où tu comprends vraiment les choses.
link: https://open.spotify.com/episode/1Y9xEnTn0yefQeAl6pv9xp
**********
title: #46 : Gouvernement : Monter la cellule data de l'Élysée
transcript: [1214.76 ====> 1241.64]  il y a énormément de contenu pour se former. 
Moi je trouve ça chouette, ça permet maintenant à  n'importe qui qui est motivé, 
qui a envie de se former, qui a envie d'avoir de l'impact je pense,  de le faire. 
Tu peux le faire en sortant d'une école, tu peux aussi le faire de ton côté  en te formant sur YouTube ou 
sur Internet et moi je trouve ça chouette.  Qu'est-ce qui t'a le plus fait progresser ?  
Qu'est-ce qui m'a fait le plus progresser ? Je pense que c'est les gens avec qui j'ai
link: https://open.spotify.com/episode/1rsJtbAyw7QBd9J2DgXZCH
**********
title: #40 - Artefact : Encadrer 40+ Data Scientists dans un marché en forte évolution
transcript: [2003.44 ====> 2030.2]  mais en tout cas la limite c'est ce  qu'on a envie d'en faire. 
Qu'est-ce qui t'a le plus fait progresser ? C'est les interactions avec  les autres. 
Aujourd'hui par exemple, je suis IP Data Science et je pense que j'apprends plus des  gens que j'encadre que moi je leur apprends de choses. Ça veut dire qu'au final, je pense que  c'est l'achievement en fait de se dire à un moment donné, t'apprends plus des gens que t'encadres  parce que ce monde
link: https://open.spotify.com/episode/3ez01Fw1EfmDiVrPqprWig
**********
title: #54 - Pernod Ricard : Lancer des programmes de Data Science
transcript: [1385.68 ====> 1406.6]  Qu'est-ce qui t'a le plus fait progresser ?  
Alors, quelqu'un à qui on a parlé dans un de tes podcasts, mais la rencontre avec les  autres.  
Ce qui est génial c'est que du coup j'ai plein de métiers différents qui travaillent  dans notre équipe, j'ai des gens vraiment avec des horizons différents et j'apprends  à chaque fois deux, donc c'est vraiment super.
link: https://open.spotify.com/episode/6h9fqfWmFl3zt0tqPfqS5R
**********
title: #49 - Masteos : Lancer le département Data par itération
transcript: [1568.64 ====> 1593.52]  de toutes les régressions et autres, 
c'est des choses que j'ai vraiment découvert sur le tas  et rapidement. 
Et sinon peut-être plus globalement, qu'est-ce qui t'a le plus fait progresser aussi en  tant que professionnel ? 
Ce n'est pas forcément que Pure Data, mais... Je pense que ce qui te  fait progresser aujourd'hui, c'est la curiosité. 
 En fait, il faut vraiment être curieux de tout,  aller voir un peu partout,
link: https://open.spotify.com/episode/4NIJcHpfkDqb1Ac5A0aAMZ
**********
```