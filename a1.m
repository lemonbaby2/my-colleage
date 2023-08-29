clear;
a=imread('peppers.png');
imshow(a);
c=im2double(a);
r=c(:,:,1);
g=c(:,:,2);
b=c(:,:,3);
ns=0.05*randn(384,512);
noise=sign(ns).*sqrt(abs(ns));
r=r+noise;
for i=1:384
    for j=1:512
        if r(i,j)>1
            r(i,j)=1;
        elseif r(i,j)<0
            r(i,j)=0;
        end
    end
end
ns=0.05*randn(384,512);
noise=sign(ns).*sqrt(abs(ns));
g=g+noise;
for i=1:384
    for j=1:512
        if g(i,j)>1
            g(i,j)=1;
        elseif g(i,j)<0
            g(i,j)=0;
        end
    end
end
ns=0.05*randn(384,512);
noise=sign(ns).*sqrt(abs(ns));
b=b+noise;
for i=1:384
    for j=1:512
        if b(i,j)>1
            b(i,j)=1;
        elseif b(i,j)<0
            b(i,j)=0;
        end
    end
end
c(:,:,1)=r;
c(:,:,2)=g;
c(:,:,3)=b;
imwrite(c,'peppers_Gaussion.png');

a=imread('peppers.png');
c=im2double(a);
noise=randsrc(384,512,[-1,0,1;0.05,0.9,0.05]);
for i=1:384
    for j=1:512
        if noise(i,j)==1
            c(i,j,:)=1;
        elseif noise(i,j)==-1
            c(i,j,:)=0;
        end
    end
end
imwrite(c,'peppers_sp.png');

%高斯白噪声的均值滤波
a=imread('peppers_Gaussion.png');
a=im2double(a);
r=a(:,:,1);
g=a(:,:,2);
b=a(:,:,3);
for i=1:384
    for j=1:512
        sumr=0;
        sumg=0;
        sumb=0;
        num=0;
        for k=i-1:i+1
            for l=j-1:j+1
                if k>=1&&k<=384&&l>=1&&l<=512
                    sumr=sumr+r(k,l);
                    sumg=sumg+g(k,l);
                    sumb=sumb+b(k,l);
                    num=num+1;
                end
            end
        end
        a(i,j,1)=sumr/num;
        a(i,j,2)=sumg/num;
        a(i,j,3)=sumb/num;
    end
end
imwrite(a,'peppers_Gaussion_Mean_3.png');
for i=1:384
    for j=1:512
        sumr=0;
        sumg=0;
        sumb=0;
        num=0;
        for k=i-2:i+2
            for l=j-2:j+2
                if k>=1&&k<=384&&l>=1&&l<=512
                    sumr=sumr+r(k,l);
                    sumg=sumg+g(k,l);
                    sumb=sumb+b(k,l);
                    num=num+1;
                end
            end
        end
        a(i,j,1)=sumr/num;
        a(i,j,2)=sumg/num;
        a(i,j,3)=sumb/num;
    end
end
imwrite(a,'peppers_Gaussion_Mean_5.png');
for i=1:384
    for j=1:512
        sumr=0;
        sumg=0;
        sumb=0;
        num=0;
        for k=i-3:i+3
            for l=j-3:j+3
                if k>=1&&k<=384&&l>=1&&l<=512
                    sumr=sumr+r(k,l);
                    sumg=sumg+g(k,l);
                    sumb=sumb+b(k,l);
                    num=num+1;
                end
            end
        end
        a(i,j,1)=sumr/num;
        a(i,j,2)=sumg/num;
        a(i,j,3)=sumb/num;
    end
end
imwrite(a,'peppers_Gaussion_Mean_7.png');

%椒盐噪声的均值滤波
a=imread('peppers_sp.png');
a=im2double(a);
r=a(:,:,1);
g=a(:,:,2);
b=a(:,:,3);
for i=1:384
    for j=1:512
        sumr=0;
        sumg=0;
        sumb=0;
        num=0;
        for k=i-1:i+1
            for l=j-1:j+1
                if k>=1&&k<=384&&l>=1&&l<=512
                    sumr=sumr+r(k,l);
                    sumg=sumg+g(k,l);
                    sumb=sumb+b(k,l);
                    num=num+1;
                end
            end
        end
        a(i,j,1)=sumr/num;
        a(i,j,2)=sumg/num;
        a(i,j,3)=sumb/num;
    end
end
imwrite(a,'peppers_sp_Mean_3.png');
for i=1:384
    for j=1:512
        sumr=0;
        sumg=0;
        sumb=0;
        num=0;
        for k=i-2:i+2
            for l=j-2:j+2
                if k>=1&&k<=384&&l>=1&&l<=512
                    sumr=sumr+r(k,l);
                    sumg=sumg+g(k,l);
                    sumb=sumb+b(k,l);
                    num=num+1;
                end
            end
        end
        a(i,j,1)=sumr/num;
        a(i,j,2)=sumg/num;
        a(i,j,3)=sumb/num;
    end
end
imwrite(a,'peppers_sp_Mean_5.png');
for i=1:384
    for j=1:512
        sumr=0;
        sumg=0;
        sumb=0;
        num=0;
        for k=i-3:i+3
            for l=j-3:j+3
                if k>=1&&k<=384&&l>=1&&l<=512
                    sumr=sumr+r(k,l);
                    sumg=sumg+g(k,l);
                    sumb=sumb+b(k,l);
                    num=num+1;
                end
            end
        end
        a(i,j,1)=sumr/num;
        a(i,j,2)=sumg/num;
        a(i,j,3)=sumb/num;
    end
end
imwrite(a,'peppers_sp_Mean_7.png');

%高斯白噪声的中值滤波
a=imread('peppers_Gaussion.png');
a=im2double(a);
r=a(:,:,1);
g=a(:,:,2);
b=a(:,:,3);
% sumr=ones(49);
% sumg=ones(49);
% sumb=ones(49);
for i=1:384
    for j=1:512
%         num=1;
%         for k=i-1:i+1
%             for l=j-1:j+1
%                 if k>=1&&k<=384&&l>=1&&l<=512
%                     sumr(num)=r(k,l);
%                     sumg(num)=g(k,l);
%                     sumb(num)=b(k,l);
%                     num=num+1;
%                 end
%             end
%         end
%         a(i,j,1)=median(sumr(1:num-1));
%         a(i,j,2)=median(sumg(1:num-1));
%         a(i,j,3)=median(sumb(1:num-1));
          a(i,j,1)=median(r(max(i-1,1):min(i+1,384),max(j-1,1):min(j+1,512)),'all');
          a(i,j,2)=median(g(max(i-1,1):min(i+1,384),max(j-1,1):min(j+1,512)),'all');
          a(i,j,3)=median(b(max(i-1,1):min(i+1,384),max(j-1,1):min(j+1,512)),'all');
    end
end
imwrite(a,'peppers_Gaussion_Median_3.png');
for i=1:384
    for j=1:512
%         num=1;
%         for k=i-2:i+2
%             for l=j-2:j+2
%                 if k>=1&&k<=384&&l>=1&&l<=512
%                     sumr(num)=r(k,l);
%                     sumg(num)=g(k,l);
%                     sumb(num)=b(k,l);
%                     num=num+1;
%                 end
%             end
%         end
%         a(i,j,1)=median(sumr(1:num-1));
%         a(i,j,2)=median(sumg(1:num-1));
%         a(i,j,3)=median(sumb(1:num-1));
          a(i,j,1)=median(r(max(i-2,1):min(i+2,384),max(j-2,1):min(j+2,512)),'all');
          a(i,j,2)=median(g(max(i-2,1):min(i+2,384),max(j-2,1):min(j+2,512)),'all');
          a(i,j,3)=median(b(max(i-2,1):min(i+2,384),max(j-2,1):min(j+2,512)),'all');
    end
end
imwrite(a,'peppers_Gaussion_Median_5.png');
for i=1:384
    for j=1:512
%         num=1;
%         for k=i-3:i+3
%             for l=j-3:j+3
%                 if k>=1&&k<=384&&l>=1&&l<=512
%                     sumr(num)=r(k,l);
%                     sumg(num)=g(k,l);
%                     sumb(num)=b(k,l);
%                     num=num+1;
%                 end
%             end
%         end
%         a(i,j,1)=median(sumr(1:num-1));
%         a(i,j,2)=median(sumg(1:num-1));
%         a(i,j,3)=median(sumb(1:num-1));
          a(i,j,1)=median(r(max(i-3,1):min(i+3,384),max(j-3,1):min(j+3,512)),'all');
          a(i,j,2)=median(g(max(i-3,1):min(i+3,384),max(j-3,1):min(j+3,512)),'all');
          a(i,j,3)=median(b(max(i-3,1):min(i+3,384),max(j-3,1):min(j+3,512)),'all');
    end
end
imwrite(a,'peppers_Gaussion_Median_7.png');

%椒盐噪声的中值滤波
a=imread('peppers_sp.png');
a=im2double(a);
r=a(:,:,1);
g=a(:,:,2);
b=a(:,:,3);
% sumr=ones(49);
% sumg=ones(49);
% sumb=ones(49);
for i=1:384
    for j=1:512
%         num=1;
%         for k=i-1:i+1
%             for l=j-1:j+1
%                 if k>=1&&k<=384&&l>=1&&l<=512
%                     sumr(num)=r(k,l);
%                     sumg(num)=g(k,l);
%                     sumb(num)=b(k,l);
%                     num=num+1;
%                 end
%             end
%         end
        a(i,j,1)=median(r(max(i-1,1):min(i+1,384),max(j-1,1):min(j+1,512)),'all');
        a(i,j,2)=median(g(max(i-1,1):min(i+1,384),max(j-1,1):min(j+1,512)),'all');
        a(i,j,3)=median(b(max(i-1,1):min(i+1,384),max(j-1,1):min(j+1,512)),'all');
    end
end
imwrite(a,'peppers_sp_Median_3.png');
for i=1:384
    for j=1:512
%         num=1;
%         for k=i-2:i+2
%             for l=j-2:j+2
%                 if k>=1&&k<=384&&l>=1&&l<=512
%                     sumr(num)=r(k,l);
%                     sumg(num)=g(k,l);
%                     sumb(num)=b(k,l);
%                     num=num+1;
%                 end
%             end
%         end
        a(i,j,1)=median(r(max(i-2,1):min(i+2,384),max(j-2,1):min(j+2,512)),'all');
        a(i,j,2)=median(g(max(i-2,1):min(i+2,384),max(j-2,1):min(j+2,512)),'all');
        a(i,j,3)=median(b(max(i-2,1):min(i+2,384),max(j-2,1):min(j+2,512)),'all');
    end
end
imwrite(a,'peppers_sp_Median_5.png');
for i=1:384
    for j=1:512
%         num=1;
%         for k=i-3:i+3
%             for l=j-3:j+3
%                 if k>=1&&k<=384&&l>=1&&l<=512
%                     sumr(num)=r(k,l);
%                     sumg(num)=g(k,l);
%                     sumb(num)=b(k,l);
%                     num=num+1;
%                 end
%             end
%         end
        a(i,j,1)=median(r(max(i-3,1):min(i+3,384),max(j-3,1):min(j+3,512)),'all');
        a(i,j,2)=median(g(max(i-3,1):min(i+3,384),max(j-3,1):min(j+3,512)),'all');
        a(i,j,3)=median(b(max(i-3,1):min(i+3,384),max(j-3,1):min(j+3,512)),'all');
    end
end
imwrite(a,'peppers_sp_Median_7.png');
a=imread('original_face.jpeg');
a=im2double(a);
r=a(:,:,1);
g=a(:,:,2);
b=a(:,:,3);
sumr=ones(49);
sumg=ones(49);
sumb=ones(49);
for i=1:752
    for j=1:500
        num=1;
        for k=i-3:i+3
            for l=j-3:j+3
                if k>=1&&k<=752&&l>=1&&l<=500
                    sumr(num)=r(k,l);
                    sumg(num)=g(k,l);
                    sumb(num)=b(k,l);
                    num=num+1;
                end
            end
        end
        a(i,j,1)=median(sumr(1:num-1));
        a(i,j,2)=median(sumg(1:num-1));
        a(i,j,3)=median(sumb(1:num-1));
    end
end
imwrite(a,'beautified_face.jpeg');
