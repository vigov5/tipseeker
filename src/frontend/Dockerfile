FROM nginx:alpine
COPY . /frontend
WORKDIR /frontend
RUN apk add --no-cache nodejs yarn npm
RUN yarn install
RUN npx --yes browserslist@latest --update-db
RUN yarn build
RUN rm -rf /usr/share/nginx/html && ln -s /frontend/public /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]