// Headless mGBA runner: ./run rom.gba script.txt outdir
// script lines: "wait N" | "press KEYS [holdFrames]" (KEYS like A, B, START, UP, A+B) | "shot NAME"
#include <mgba/core/core.h>
#include <mgba/core/log.h>
#include <mgba/gba/interface.h>
#include <mgba-util/vfs.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static void nolog(struct mLogger* l, int c, enum mLogLevel lv, const char* f, va_list a){}
static struct mLogger logger = { .log = nolog };
static int keymask(char *s){ int m=0; char *t=strtok(s,"+"); while(t){
  if(!strcmp(t,"A"))m|=1<<0; else if(!strcmp(t,"B"))m|=1<<1; else if(!strcmp(t,"SELECT"))m|=1<<2;
  else if(!strcmp(t,"START"))m|=1<<3; else if(!strcmp(t,"RIGHT"))m|=1<<4; else if(!strcmp(t,"LEFT"))m|=1<<5;
  else if(!strcmp(t,"UP"))m|=1<<6; else if(!strcmp(t,"DOWN"))m|=1<<7; else if(!strcmp(t,"R"))m|=1<<8; else if(!strcmp(t,"L"))m|=1<<9;
  t=strtok(NULL,"+");} return m; }
int main(int argc,char**argv){
  mLogSetDefaultLogger(&logger);
  struct mCore* core = mCoreFind(argv[1]); if(!core){puts("no core");return 1;}
  core->init(core); mCoreInitConfig(core,NULL);
  unsigned w,h; core->desiredVideoDimensions(core,&w,&h);
  color_t* buf = malloc(w*h*sizeof(color_t)); core->setVideoBuffer(core,buf,w);
  if(!mCoreLoadFile(core,argv[1])){puts("load fail");return 1;}
  core->reset(core);
  FILE* f=fopen(argv[2],"r"); char line[256]; long frame=0;
  while(fgets(line,sizeof line,f)){
    char cmd[32],arg[64]; int n=0; arg[0]=0; if(sscanf(line,"%31s %63s %d",cmd,arg,&n)<1||cmd[0]=='#')continue;
    if(!strcmp(cmd,"wait")){int k=atoi(arg);core->setKeys(core,0);while(k--){core->runFrame(core);frame++;}}
    else if(!strcmp(cmd,"press")){int hold=n>0?n:4;core->setKeys(core,keymask(arg));while(hold--){core->runFrame(core);frame++;}core->setKeys(core,0);for(int i=0;i<4;i++){core->runFrame(core);frame++;}}
    else if(!strcmp(cmd,"shot")){char p[512];snprintf(p,sizeof p,"%s/%s.raw",argv[3],arg);FILE*o=fopen(p,"wb");
      for(unsigned i=0;i<w*h;i++){color_t c=buf[i];unsigned char px[3]={c&0xFF,(c>>8)&0xFF,(c>>16)&0xFF};fwrite(px,1,3,o);}fclose(o);}
  }
  printf("frames %ld\n",frame); return 0;
}
