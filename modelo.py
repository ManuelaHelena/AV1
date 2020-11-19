from config import *

class Cachorro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    raça = db.Column(db.String(254))
    porte = db.Column(db.String(254))
    pelagem = db.Column(db.String(254))
    def __str__(self):
        return str(self.id) + ", " + self.nome + ", " + self.raça + ", " + self.porte + ", " + self.pelagem
    def json(self):
        return {
            "id" : self.id,
            "nome" : self.nome,
            "raça" : self.raça ,
            "porte" : self.porte,
            "pelagem" : self.pelagem
        }
if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)
    db.create_all()

    nova = Cachorro(nome = "téo", raça = "shitzu",
                    porte = "pequeno", pelagem = "média")
    db.session.add(nova)
    db.session.commit()
    todas = db.session.query(Cachorro).all()
    for p in todas:
        print(p)
        print(p.json())
    #print(nova.nome)