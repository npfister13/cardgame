if file == png:
  ...
elif file == jpg:
  ...
  
class PoisonStrategy extend UploadStrategy:
  ability = 'poison'
  
  def applyDamage(attackingCard, receivingCard):
    ...
    
class ShieldStrategy extend UploadStrategy:
  ability = 'shield'

  def applyDamage(attackingCard, receivingCard):
    ...

interface AbilityStrategy:
  def applyDamage(attackingCard, receivingCard)
  
########

uploaderStrategies = [PngUploadStrategy(), JpgUploadStrategy()]

for strategy in uploaderStrategies:
  if strategy.ability == mimeType:
    strategy.applyDamage(attackingCard, receivingCard)

    
#####