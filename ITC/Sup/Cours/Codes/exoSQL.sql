select nom, prénom
from c
where établissement = "Faidherbe"

select nom, prénom
from e
where classe = "MPSI4"

select matiere
from n
where date = "07/12/19"

select classe, count()
from e
group by classe

select matiere, min(note), max(note), avg(note)
from n
group by matiere


select n.matiere, min(n.note), max(n.note), avg(n.note)
from n join e on n.etu = e.id
where e.classe = "MPSI5"
group by n.matiere

select établissement, count() as nb_colleurs
from c
group by établissement
having nb_colleurs >= 30

select n.note, count()
from c join n on c.id = n.clr
where c.nom = "de Boisseson" 
group by n.note

select e.nom, e.prenom, count() as nb_20
from n join e on n.etu = e.id
where n.note = 20
group by e.id

select distinct n.matiere
from n join e on n.etu = e.id
where e.classe = "MPSI1"

select distinct c.nom
from c join n on c.id = n.clr
       join e on n.etu = e.id
where e.classe = "PCSI2"

select e. nom, e.prénom, n.date, n.note
from c join n join e on (c.id = n.clr and n.etu = e.id)
where c.nom = "Hoguet" and c.prénom = "Stéphane"
                       and e.classe = "MPSI3"

select avg(n.note)
from n join e on n.etu = e.id
where n.matière = "Math" and e.classe = "MPSI2"

select e.nom, e.prénom, avg(n.note)
from n join e on n.etu = e.id
where n.matière = "Math" and e.classe = "MPSI2"
group by e.id

select c.nom, max(n.note) as max_phys
from n join c on c.id = n.clr
where n.matière = "Phys"
group by c.nom
having max_phys >= 18

select e.nom, e.prenom, min(n.note) as min_chim
from e join n on e.id = n.etu
where n.matiere = "Chim" and e.classe = "PCSI1"
group by e.id
having min_chim >= 15

/* Exercice 19 */
/* Première méthode, sans les notes */
(select e.nom, e.prénom
from n join e on n.etu = e.id
where n.matière = "Math" and e.classe = "MPSI1"
group by e.id
having avg(n.note) >= (select avg(n.note)
                    from n join e on n.etu = e.id
                     where n.matière = "Math" 
                          and e.classe = "MPSI1"))

intersect
 
(select e.nom, e.prénom
from n join e on n.etu = e.id
where n.matière = "Phys" and e.classe = "MPSI1"
group by e.id
having avg(n.note) >= (select avg(n.note)
                    from n join e on n.etu = e.id
                     where n.matière = "Phys" 
                          and e.classe = "MPSI1"))
                          
                          
/* Deuxième méthode, avec  les notes */
select m.nom, p.prenom, m.moy_math, p.moy_phys
from 
(select e.id as id, e.nom as nom, e.prénom as prenom , 
                   avg(n.note) as moy_math
from n join e on n.etu = e.id
where n.matière = "Math" and e.classe = "MPSI1"
group by e.id
having moy_math >= (select avg(n.note)
                    from n join e on n.etu = e.id
                     where n.matière = "Math" 
                          and e.classe = "MPSI1")) as m
join
(select e.id as id, e.nom as nom, e.prénom as prenom , 
                   avg(n.note) as moy_phys
from n join e on n.etu = e.id
where n.matière = "Phys" and e.classe = "MPSI1"
group by e.id
having moy_math >= (select avg(n.note)
                    from n join e on n.etu = e.id
                     where n.matière = "Phys" 
                          and e.classe = "MPSI1")) as p
on m.id = p.id
















