import asyncio
import pytest

def test_arun_to_summary():
    from src.utils.llm_text import LlmText
    
    text = LlmText(object="Global variables can be accessed from within functions, but we cannot set them without explicitly naming them as global inside the function. foo ...")
    
    async def run():
        test = await text.arun_to_summary()
        
        print("summary",test)

    asyncio.run(run())

def test_arun_to_triplets():
    from src.utils.llm_text import LlmText
    
    text = LlmText(object="""The giant panda (Ailuropoda melanoleuca), also known as the panda bear or simply panda, is a bear species endemic to China. It is characterised by its black-and-white coat and rotund body. The name "giant panda" is sometimes used to distinguish it from the red panda, a neighboring musteloid. Adult individuals average 100 to 115 kg (220 to 254 lb), and are typically 1.2 to 1.9 m (3 ft 11 in to 6 ft 3 in) long. The species is sexually dimorphic, as males are typically 10 to 20% larger. The fur is white, with black patches around the eyes, ears, legs and shoulders. A thumb is visible on the bear's forepaw, which helps in holding bamboo in place for feeding. Giant pandas have adapted larger molars and expanded temporal fossa to meet their dietary requirements.

The giant panda is exclusively found in six mountainous regions in a few provinces. It is also found in elevations of up to 3,000 m (9,800 ft). Its diet consists almost entirely of bamboo, making the bear mostly herbivorous, despite being classified in the order Carnivora. The shoot is an important energy source, as it contains starch and is 32% protein, hence pandas evolved the ability to effectively digest starch. They are solitary, only gathering in times of mating. Females rear cubs for an average of 18 to 24 months. Potential predators of sub-adult pandas include leopards. Giant pandas heavily rely on olfactory communication to communicate with one another; scent marks are used as chemical cues and on landmarks like rocks or trees. Giant pandas live long lives, with the oldest known individual dying at 38.

As a result of farming, deforestation, and other development, the giant panda has been driven out of the lowland areas where it once lived, and it is a conservation-reliant vulnerable species. A 2007 report showed 239 pandas living in captivity inside China and another 27 outside the country. Some reports also show that the number of giant pandas in the wild is on the rise. By March 2015, the wild giant panda population had increased to 1,864 individuals. In 2016, it was reclassified on the IUCN Red List from "endangered" to "vulnerable", affirming decade-long efforts to save the panda. In July 2021, Chinese authorities also reclassified the giant panda as vulnerable. The giant panda has often served as China's national symbol, appeared on Chinese Gold Panda coins since 1982 and as one of the five Fuwa mascots of the 2008 Summer Olympics held in Beijing.""")
    
    async def run():
        test = await text.arun_to_triplets(query="Extract triplets from this text. 1 triplet per sentence")
        
        print("triplets",test)
        
    asyncio.run(run())