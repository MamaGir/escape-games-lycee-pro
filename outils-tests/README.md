# outils-tests — tests automatiques des escape games du lycée pro (Node + jsdom)

Chaque jeu a un dossier `tests/` : une partie complète est jouée **sans navigateur**, comme le ferait une équipe, au niveau Essentiel puis Expert, avec des erreurs volontaires.

| Fichier | Rôle |
|---|---|
| `charge.js` | ouvre une page dans jsdom, sans réseau (scripts et `fetch` lus sur le disque) |
| `moteur-commun.js` | tests des jeux à moteur commun : tout est déduit de `enigmes.json` |
| `tous.js` | lance tous les tests, jeu après jeu (et `commun/tests/`), avec un tableau récapitulatif |
| `verifier-enigmes.js` | contrôle des énigmes avant publication |
| `verifier-liens-internes.js` | tous les liens internes mènent à un fichier existant |
| `<jeu>/tests/test-jeu.js` | le test d'un jeu |
| `commun/tests/` | cohérence du moteur et de la page de vérification, énigmes, hors connexion, archives, pages du lycée |

## Lancer les tests (Windows)

**Outil : l'Invite de commandes**, avec **Node.js** installé (https://nodejs.org, version LTS, options par défaut).

1. Touche **Windows + R**, taper `cmd`, **Entrée**.
2. `cd "<dossier du dépôt>"`.
3. **Une seule fois** : `cd outils-tests`, `npm install`, `cd ..` (le dossier `node_modules` n'est pas publié).
4. `node outils-tests\tous.js` (ou un seul jeu : `node outils-tests\tous.js pates-ceramiques`).
5. Lire la dernière ligne : **« Tous les tests passent »**. Sinon, les lignes ✗ disent quoi.

Version immersive : `node immersifs\pates-ceramiques\tests\test-immersif.js`.
