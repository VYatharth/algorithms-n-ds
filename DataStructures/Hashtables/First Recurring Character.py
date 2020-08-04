class RecurringCharacter():
    @staticmethod
    def find_first_recurring_char(data):
        existing_characters = {};
        
        for character in data:
            if character not in existing_characters:
                existing_characters[character] = 1;
            else:
                return character

        return None


print(RecurringCharacter.find_first_recurring_char([1,3,4,2,5]))

