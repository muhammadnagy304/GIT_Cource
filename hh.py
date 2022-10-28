print("\n\n\n ")
class skill:

  def __init__(self):
    self.skills = ["Python", "Css", "C"]

  def __str__(self):
    return f"{self.skills}"

  def __len__(self):
    return len(self.skills)

profile = skill()
print(f"{profile.skills}")
print(profile)
print(len(profile))
profile.skills.append("C++")
print(len(profile))
