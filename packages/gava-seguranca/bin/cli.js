#!/usr/bin/env node
'use strict';

/*
 * gava-seguranca — instala a auditoria de conformidade LGPD no projeto atual.
 * Uso:
 *   npx gava-seguranca init         # copia AGENTS-lgpd.md + seguranca/ para o cwd
 *   npx gava-seguranca init --force # sobrescreve arquivos existentes
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

function init() {
  log('\n🔐 Instalando a auditoria de conformidade LGPD neste projeto...\n');

  // 1. Instruções de auditoria na raiz (lidas por Cursor, Copilot, Windsurf, Codex, etc.)
  copyFile(path.join(ASSETS, 'AGENTS-lgpd.md'), 'AGENTS-lgpd.md');

  // 2. Referências detalhadas em seguranca/references/
  const refDir = path.join(ASSETS, 'references');
  if (fs.existsSync(refDir)) {
    for (const f of fs.readdirSync(refDir)) {
      copyFile(path.join(refDir, f), path.join('seguranca', 'references', f));
    }
  }

  // 3. Scanner automático de PII
  copyFile(path.join(ASSETS, 'scan_pii.py'), path.join('seguranca', 'scan_pii.py'));

  log('\n✅ Pronto!');
  log('   • AGENTS-lgpd.md na raiz — peça ao agente da sua IDE para segui-lo numa auditoria.');
  log('   • seguranca/references/ — checklists de tokenização, criptografia e detecção.');
  log('   • seguranca/scan_pii.py — primeira passada: python seguranca/scan_pii.py .');
  log('\n   Dica: se a sua IDE só lê AGENTS.md, aponte o agente para o AGENTS-lgpd.md');
  log('   ou cole o conteúdo dele no seu AGENTS.md quando for auditar.\n');
}

function help() {
  log('\ngava-seguranca — auditoria de conformidade LGPD para pipelines fiscais\n');
  log('Uso:');
  log('  npx gava-seguranca init           Instala AGENTS-lgpd.md + seguranca/ no projeto');
  log('  npx gava-seguranca init --force   Sobrescreve arquivos existentes');
  log('  npx gava-seguranca help           Mostra esta ajuda\n');
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
