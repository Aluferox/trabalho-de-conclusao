import subprocess


def handle_uploaded_file(sequencias):
    path = '/tmp/sequencia.txt'

    if isinstance(sequencias,str):
        sequencias = sequencias.split('\r\n')
        with open(path, 'w') as file:
            for sequencia in sequencias:
                file.write(f'{sequencia}\n')
        file.close()
    else:
        with open(path, 'wb+') as destination:
            for chunk in sequencias.chunks():
                destination.write(chunk)

        destination.close()

    stdout = subprocess.run(['/home/alufer/Área de Trabalho/RepositoriosGitHub/deployer_astar/astar_msa/bin/msa_astar', path],
                             stdout=subprocess.PIPE, encoding='utf8')

    result = stdout.stdout.split('\n')
    if len(result) > 4:
        phase_one = result[1][26:35]
        phase_two = result[4][30:39]
        similarity = result[6][11:18]
        result = [strip for strip in result[8:] if strip != '']
        result = result[:-1]

        return result, [phase_one, phase_two, similarity]
    else:
        return [], []