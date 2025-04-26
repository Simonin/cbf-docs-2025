import os, glob, math

# quantos arquivos por parte
BATCH_SIZE = 4

# lista todos os .md em docs/
docs = sorted(glob.glob('docs/*.md'))
num_parts = math.ceil(len(docs) / BATCH_SIZE)

for i in range(num_parts):
    part_docs = docs[i*BATCH_SIZE:(i+1)*BATCH_SIZE]
    filename = f'compiled_part{i+1}.md'
    with open(filename, 'w', encoding='utf-8') as out:
        for path in part_docs:
            name = os.path.basename(path)
            out.write(f'<!--- DOCUMENTO: {name} --->\n\n')
            with open(path, 'r', encoding='utf-8') as f:
                out.write(f.read())
            out.write('\n\n')
    print(f'✅ Gerado {filename} com {len(part_docs)} documentos.')

