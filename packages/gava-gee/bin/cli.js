#!/usr/bin/env node
'use strict';

/*
 * gava-gee — instala a referência da API do Google Earth Engine no projeto atual.
 * Uso:
 *   npx gava-gee init         # copia AGENTS-gee.md + gee/ para o cwd
 *   npx gava-gee init --force # sobrescreve arquivos existentes
 */

const fs = require('fs');
const path = require('path');

const PKG_ROOT = path.resolve(__dirname, '..');
const ASSETS = path.join(PKG_ROOT, 'assets');
const CWD = process.cwd();

const args = process.argv.slice(2);
const cmd = args[0];
const force = args.includes('--force') || args.includes('-f');

function log(msg) { process.stdout.write(msg + '\n'); }

function copyFile(src, destRel) {
  const dest = path.join(CWD, destRel);
  if (fs.existsSync(dest) && !force) {
    log('  ⏭  já existe (use --force para sobrescrever): ' + destRel);
    return;
  }
  fs.mkdirSync(path.dirname(dest), { recursive: true });
  fs.copyFileSync(src, dest);
  log('  ✓  ' + destRel);
}

// Copia uma pasta recursivamente, preservando a estrutura, para destRelDir.
function copyDir(srcDir, destRelDir) {
  if (!fs.existsSync(srcDir)) return;
  for (const entry of fs.readdirSync(srcDir, { withFileTypes: true })) {
    const src = path.join(srcDir, entry.name);
    const destRel = path.join(destRelDir, entry.name);
    if (entry.isDirectory()) {
      copyDir(src, destRel);
    } else {
      copyFile(src, destRel);
    }
  }
}

function init() {
  log('\n🌍 Instalando a referência do Google Earth Engine neste projeto...\n');

  // 1. Instruções na raiz (lidas por Cursor, Copilot, Windsurf, Codex, etc.)
  copyFile(path.join(ASSETS, 'AGENTS-gee.md'), 'AGENTS-gee.md');

  // 2. Cheatsheet, referência completa e exemplos em gee/
  copyFile(path.join(ASSETS, 'cheatsheet.md'), path.join('gee', 'cheatsheet.md'));
  copyDir(path.join(ASSETS, 'references'), path.join('gee', 'references'));
  copyDir(path.join(ASSETS, 'examples'), path.join('gee', 'examples'));

  log('\n✅ Pronto!');
  log('   • AGENTS-gee.md na raiz — aponte o agente da sua IDE para ele ao escrever código GEE.');
  log('   • gee/cheatsheet.md — as ~35 funções essenciais.');
  log('   • gee/references/ — API completa (1.747 funções) fatiada por tarefa.');
  log('   • gee/examples/ — pipeline fim-a-fim comentado.');
  log('\n   Dica: se a sua IDE só lê AGENTS.md, aponte o agente para o AGENTS-gee.md');
  log('   ou cole o conteúdo dele no seu AGENTS.md quando for trabalhar com GEE.\n');
}

function help() {
  log('\ngava-gee — referência da API do Google Earth Engine para qualquer IDE\n');
  log('Uso:');
  log('  npx gava-gee init           Instala AGENTS-gee.md + gee/ no projeto');
  log('  npx gava-gee init --force   Sobrescreve arquivos existentes');
  log('  npx gava-gee help           Mostra esta ajuda\n');
}

switch (cmd) {
  case 'init': init(); break;
  case 'help':
  case '--help':
  case '-h':
  case undefined: help(); break;
  default:
    log('Comando desconhecido: ' + cmd);
    help();
    process.exit(1);
}
