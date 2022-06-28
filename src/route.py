class Route:
    
    def __init__(self,googleRoute,pois, rank_user = None):
        self.google_route = googleRoute #rota inicial google
        self.pois = pois #pontos de interesse
        self.scores = [] #scores das predições de cada poi na rota
        self.rec_score = 0.0 #score final soma_dos_scores / qtd_pois
        self.rank_user = rank_user # avaliação realmente predita do usuário
        self.rank = 0 