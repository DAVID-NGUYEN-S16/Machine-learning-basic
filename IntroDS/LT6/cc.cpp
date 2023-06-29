#include <stdio.h>
#include <string.h>
#define max 100

typedef struct SINHVIEN
{
	char HoLot[30];
	char Ten[30];
	char Ngaysinh[20];
	char Noisinh[40];
	float D_WIN;
	float D_WORD;
	float D_EXCEL;
	float TONGDIEM;
	char X_LOAI[20];
} SV;
	void inputIn4_1sv(SV &sv);
	void inputDiem_1sv(SV &sv);
	void inputIn4_sv(SV sv[], int &n);
	void inputDiem_sv(SV sv[], int &n);
	void outputIn4_sv (SV sv[], int n);
	void outputIn4_1sv (SV sv, int n);

int main()
{
	SV sv[max];
	int n;
	printf("Nhap so luong sinh vien:"); scanf("%d", &n);
	printf("NHAP THONG TIN SINH VIEN:"); inputIn4_sv(sv, n);
	//printf("\nNHAP DIEM CUA SINH VIEN:"); inputDiem_sv(sv, n);
	outputIn4_sv (sv, n);
}
	void outputIn4_sv (SV sv[], int n){
		for (int i=0; i<n; i++){
			outputIn4_1sv (sv[i], n);
		}
	}
	
	void outputIn4_1sv (SV sv, int n){
		strcat(sv.HoLot, " ");
		printf("\n|%-20s|%-20s|%-20s|%-10s|", strcat(sv.HoLot, sv.Ten), sv.Ngaysinh, sv.Noisinh, "........");
	}
	
	void inputIn4_sv(SV sv[], int &n){
		for (int i=0; i<n; i++){
			printf("\n\nSinh vien thu %d", i+1);
			inputIn4_1sv(sv[i]);
		}
	}
	
	void inputDiem_sv(SV sv[], int &n){
		for (int i=0; i<n; i++){
			printf("\nNhap diem sv thu %d", i+1 );
			inputDiem_1sv(sv[i]);
		}
	}

	void inputIn4_1sv(SV &sv) 
	{
		printf("\nNhap Ho lot:"); 
		fflush(stdin);
		gets(sv.HoLot);
		printf("Nhap ten:"); 
        scanf("%s", sv.Ten);
		printf("Nhap ngay sinh:"); 
        scanf("%s", sv.Ngaysinh);
		printf("Nhap noi sinh:"); 
		fflush(stdin);
		gets(sv.Noisinh);
		
	}
	
	void inputDiem_1sv(SV &sv)
	{
		int chon;
		do{
			printf("\n1. Nhap diem WIN "); 
			printf("\n2. Nhap diem WORD");
			printf("\n3. Nhap diem EXCEL ");
			printf("\n4. Nhap diem sinh vien khac");
			printf("\nNhap su lua chon:"); scanf("%d", &chon);
		
			switch(chon){
				case 1: {
							printf("Nhap diem WIN: "); scanf("%f", &sv.D_WIN);
				}	break;
				case 2: {
							printf("Nhap diem WORD: "); scanf("%f", &sv.D_WORD);
				}	break;
				case 3: {
							printf("Nhap diem EXCEL: "); scanf("%f", &sv.D_EXCEL);
				}	break;
			}
		} while (chon<4);
	}
