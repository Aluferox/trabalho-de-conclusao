import subprocess


def handle_uploaded_file(sequencias):
    path = '/tmp/sequencia.txt'

    if isinstance(sequencias,str):
        sequencias = sequencias.split('\r\n')

        cont=0
        with open(path, 'w') as file:
            for sequencia in sequencias:
                cont+=1
                file.write(f'>{cont}\n'+sequencia+'\n')
        file.close()
    else:
        with open(path, 'wb+') as destination:
            for chunk in sequencias.chunks():
                destination.write(chunk)

        destination.close()
    # stdout = subprocess.run(['/home/alufer/Downloads/astar_msa/bin/msa_astar', path],
    #                        stdout=subprocess.PIPE, encoding='utf8')

    stdout = subprocess.run(['/home/ubuntu/deployer_astar/astar_msa/bin/msa_astar', path],
                             stdout=subprocess.PIPE, encoding='utf8')

    result = stdout.stdout.split('\n')
    phase_one = result[1][26:35]
    phase_two = result[4][30:39]
    similarity = result[6][11:18]
    result = [strip for strip in result[8:] if strip != '']
    result = result[:-1]

    return result, [phase_one, phase_two, similarity]
