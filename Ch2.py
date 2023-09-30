class Player:
  def play(self):
    print("The player is playing ")
class Batsman(Player):
  def play(self):
    print("The Batsman is Batting ")
class Bowler(Player):
  def play(self):
    print("The Bowler is Bowling ")
batsman = Batsman()
bowler = Bowler()
batsman.play()
bowler.play()