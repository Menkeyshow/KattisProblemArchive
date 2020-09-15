# https://open.kattis.com/problems/ptice
adrian_seq = ["A", "B", "C"]
bruno_seq = ["B", "A", "B", "C"]
goran_seq = ["C", "C", "A", "A", "B", "B"]

def applicant(seq: list):
    n = 0
    while n < len(seq):
        yield seq[n]
        n += 1
    yield next(applicant(seq))

adrian = applicant(adrian_seq)
bruno = applicant(bruno_seq)
goran = applicant(goran_seq)

n_questions = input()
exam = input()
exam.split()