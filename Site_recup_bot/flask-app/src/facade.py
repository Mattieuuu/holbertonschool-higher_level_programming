from typing import List, Dict
from datetime import datetime
import json
import os

class Event:
    def __init__(self, name: str, date: str, location: str, link: str):
        self.name = name
        self.date = date
        self.location = location
        self.link = link

    def to_dict(self) -> Dict:
        return {
            'name': self.name,
            'date': self.date,
            'location': self.location,
            'link': self.link
        }

class Facade:
    def __init__(self):
        self.events: List[Event] = []
        self.data_file = os.path.join(os.path.dirname(__file__), 'data', 'events.json')
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        self.load_events()

    def save_events(self):
        events_data = [event.to_dict() for event in self.events]
        with open(self.data_file, 'w') as f:
            json.dump(events_data, f, indent=2)

    def load_events(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                try:
                    events_data = json.load(f)
                    self.events = [Event(**event) for event in events_data]
                except json.JSONDecodeError:
                    self.events = []
        else:
            self.events = []

    def add_event(self, event: Event = None) -> Event:
        if event is None:
            print("\n=== Ajouter un nouvel événement ===")
            name = input("Nom de l'événement: ")
            date = input("Date de l'événement (JJ/MM/AAAA): ")
            location = input("Lieu de l'événement: ")
            link = input("Lien de l'événement: ")

            event = Event(name, date, location, link)
        self.events.append(event)
        self.save_events()
        return event

    def get_all_events(self) -> List[Dict]:
        return [event.to_dict() for event in self.events]

    def delete_event(self, index: int):
        if 0 <= index < len(self.events):
            self.events.pop(index)
            self.save_events()

    def run(self):
        while True:
            print("\n=== Menu des événements ===")
            print("1. Ajouter un événement")
            print("2. Voir tous les événements")
            print("3. Quitter")
            
            choice = input("\nChoisissez une option (1-3): ")
            
            if choice == "1":
                self.add_event()
            elif choice == "2":
                events = self.get_all_events()
                if not events:
                    print("\nAucun événement enregistré.")
                else:
                    print("\n=== Liste des événements ===")
                    for i, event in enumerate(events, 1):
                        print(f"\nÉvénement {i}:")
                        print(f"Nom: {event['name']}")
                        print(f"Date: {event['date']}")
                        print(f"Lieu: {event['location']}")
                        print(f"Lien: {event['link']}")
            elif choice == "3":
                break
            else:
                print("Option invalide. Veuillez réessayer.")

if __name__ == '__main__':
    facade = Facade()
    facade.run()
