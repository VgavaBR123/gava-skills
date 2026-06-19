#!/usr/bin/env node
'use strict';

/*
 * gava-sdd — instala os arquivos de Spec-Driven Development no projeto atual.
 * Uso:
 *   npx gava-sdd init        # copia AGENTS.md + specs/templates/ para o cwd
 *   npx gava-sdd init --force # sobrescreve arquivos existentes
 */

const fs = require('fs');
const path = require('path');

const PKG_ROOT = path.resolve(__dirname, '..');
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
  log('\n🌱 Instalando Spec-Driven Development neste projeto...\n');

  // 1. AGENTS.md na raiz (lido por Cursor, Copilot, Windsurf, Codex, etc.)
  copyFile(path.join(PKG_ROOT, 'portable', 'AGENTS.md'), 'AGENTS.md');

  // 2. Templates em specs/templates/
  const tplDir = path.join(
    PKG_ROOT, 'plugins', 'sdd-plugin', 'skills',
    'spec-driven-development', 'templates'
  );
  if (fs.existsSync(tplDir)) {
    for (const f of fs.readdirSync(tplDir)) {
      copyFile(path.join(tplDir, f), path.join('specs', 'templates', f));
    }
  }

  // 3. Referência EARS junto dos templates (citada pelo spec-template.md)
  const earsRef = path.join(
    PKG_ROOT, 'plugins', 'sdd-plugin', 'skills',
    'spec-driven-development', 'reference', 'ears-syntax.md'
  );
  if (fs.existsSync(earsRef)) {
    copyFile(earsRef, path.join('specs', 'templates', 'reference', 'ears-syntax.md'));
  }

  log('\n✅ Pronto! O AGENTS.md está na raiz e os templates em specs/templates/.');
  log('   Sua IDE já vai conduzir o desenvolvimento via SDD.');
  log('   Comece pedindo ao agente: "Cria a constituição do projeto".\n');
}

function help() {
  log('\ngava-sdd — Spec-Driven Development scaffold\n');
  log('Uso:');
  log('  npx gava-sdd init           Instala AGENTS.md + specs/templates/ no projeto');
  log('  npx gava-sdd init --force   Sobrescreve arquivos existentes');
  log('  npx gava-sdd help           Mostra esta ajuda\n');
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
