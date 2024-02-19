from models import Gatunek, DaneWlasciwosciMechanicznych, DaneSkladuChemicznego, DaneWlasciwosciFizycznych, Komentarze
import csv


def import_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Gatunek.objects.create(
                Id_gatunku=row['Id_gatunku'],
                gatunek=row['gatunek'],
                Id_właściwości_mechanicznych=row['Id_właściwości_mechanicznych'],
                Id_właściwości_fizycznych=row['Id_właściwości_fizycznych'],
                Id_składu_chemicznego=row['Id_składu_chemicznego'],
                Id_komentarza=row['Id_komentarza'],
            )


if __name__ == '__main__':
    csv_file_path = r'C:\Users\pompeczka20\Desktop\magisterka\dane\main exc\Gatunek.csv'
    import_data(csv_file_path)
