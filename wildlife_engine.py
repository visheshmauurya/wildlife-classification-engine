# Wildlife Knowledge Base
wildlife_data = {
 "tiger": {
 "category": "Mammal",
 "diet": "Carnivore",
 "lifespan": "10–15 years",
 "habitat": "Tropical forests, grasslands, mangroves",
 "color_patterns": "Orange coat with black vertical stripes",
 "special_features": [
 "Strongest big cat",
 "Excellent night vision",
 "Solitary hunter"
 ],
 "average_weight": "90–300 kg"
 },
 "elephant": {
 "category": "Mammal",
 "diet": "Herbivore",
 "lifespan": "60–70 years",
 "habitat": "Forest, savannah, grasslands",
 "color_patterns": "Grey thick skin",
 "special_features": [
 "Largest land mammal",
 "Highly intelligent",
 "Uses trunk for tools and food"
 ],
 "average_weight": "2000–6000 kg"
 },
 "lion": {
 "category": "Mammal",
 "diet": "Carnivore",
 "lifespan": "12–16 years",
 "habitat": "Grasslands, savannahs",
 "color_patterns": "Golden coat, males have a mane",
 "special_features": [
 "Lives in prides",
 "Powerful roar",
 "Top predator"
 ],
 "average_weight": "120–250 kg"
 },
 "wolf": {
 "category": "Mammal",
 "diet": "Carnivore",
 "lifespan": "8–13 years",
 "habitat": "Forests, tundra, mountains",
 "color_patterns": "Grey, black or white fur",
 "special_features": [
 "Pack hunter",
 "Strong sense of smell",
 "Long-distance stamina"
 ],
 "average_weight": "25–60 kg"
 },
 "zebra": {
 "category": "Mammal",
 "diet": "Herbivore",
 "lifespan": "20–30 years",
 "habitat": "Grasslands",
 "color_patterns": "Black and white stripes",
 "special_features": [
 "Unique stripe pattern",
 "Strong herd instincts",
 "Fast runner"
 ],
 "average_weight": "200–450 kg"
 },
 "panda": {
 "category": "Mammal",
 "diet": "Omnivore (mainly bamboo)",
 "lifespan": "20 years",
 "habitat": "Mountain forests",
 "color_patterns": "Black and white fur",
 "special_features": [
 "Strong jaws for bamboo",
 "Gentle behavior",
 "Rare/endangered species"
 ],
 "average_weight": "70–120 kg"
 },
 "peacock": {
 "category": "Bird",
 "diet": "Omnivore",
 "lifespan": "15–20 years",
 "habitat": "Grasslands, farms, forests",
 "color_patterns": "Bright blue/green feathers",
 "special_features": [
 "Large colorful tail fan",
 "National bird of India"
 ],
 "average_weight": "4–6 kg"
 }
}
# SEARCH BOX (CLI LOOP)
print("=======================================================")
print(" 🔍 WILDLIFE CLASSIFICATION SEARCH ENGINE ")
print("=======================================================")
print("Type an animal name and press ENTER.")
print("Type EXIT to stop.\n")
while True:
 print("-------------------------------------------------------")
 animal = input("🔍 Search Animal: ").lower().strip() # CLI search box
 print("-------------------------------------------------------")
 if animal == "exit":
 print("\n🔚 Exiting Wildlife Search Engine. Goodbye!")
 break
 if animal in wildlife_data:
 info = wildlife_data[animal]
 print(f"\n📌 RESULT: {animal.upper()}")
 print("-------------------------------------------------------")
 print(f"Category : {info['category']}")
 print(f"Diet : {info['diet']}")
 print(f"Lifespan : {info['lifespan']}")
 print(f"Habitat : {info['habitat']}")
 print(f"Color Pattern : {info['color_patterns']}")
 print(f"Average Weight : {info['average_weight']}")
 print("\nSpecial Features:")
 for i, feat in enumerate(info["special_features"], 1):
 print(f" {i}. {feat}")
 print("\n")
 else:
 print(f"❌ '{animal}' not found in database.")
 print("Available animals:", ", ".join(wildlife_data.keys()))
 print("\n")
