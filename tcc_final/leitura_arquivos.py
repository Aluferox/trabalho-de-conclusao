import subprocess

def handling_tasks(task_result):
    task_result = task_result.split('\n')

    phase_one = task_result[1][26:35]
    phase_two = task_result[4][30:39]
    similarity = task_result[6][11:18]
    result = [strip for strip in task_result[8:] if strip != '']
    result = result[:-1]

    return result, [phase_one, phase_two, similarity]

