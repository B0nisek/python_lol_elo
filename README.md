# python_lol_elo

for the sake of simplicity Master, Grandmaster and Challenger tiers are omitted

Division UP -> 140 (Platinum III -> Platinum II)

League UP -> 160 (Silver I -> Gold IV)

**LolLpCalculator.calculate_lp(league_from, division_from, league_to, division_to):**

  calculates LP needed to go from given league and division to given league and division

5 Leagues - Iron, Bronze, Silver, Gold, Platinum, Diamond

4 Divisions in each league

To rank up in the same League between divisions you need 100LP + win BO3, so 2 wins, each counted for 20LP -> 140LP

To rank up between Leagues you need 100LP + win BO5, so 3 wins, each counted for 20LP -> 160LP
